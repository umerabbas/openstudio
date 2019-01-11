# -*- coding: utf-8 -*-

from gluon import *

class AccountingCashbooksItems:
    def list(self, date_from, date_until, booking_type='debit'):
        """
        List cashbook items, debit (in) or credit (out)
        :param item_type: one of ['debit', 'credit']
        :param date_from: datetime.date
        :param date_until: datetime.date
        :return: gluon.dal.rows object of Cashbook Items
        """
        db = current.db

        query = (db.accounting_cashbooks_items.BookingType == booking_type)
        rows = db(query).select(db.accounting_cashbooks_items.ALL,
                                orderby=db.accounting_cashbooks_items.BookingDate)

        return rows


    def list_formatted(self, date_from, date_until, booking_type='debit'):
        """
        List cashbook items, debit (in) or credit (out)
        :param item_type: one of ['debit', 'credit']
        :param date_from: datetime.date
        :param date_until: datetime.date
        :return: HTML table
        """
        T = current.T
        auth = current.auth
        rows = self.list(date_from, date_until, booking_type)

        permission_edit = auth.has_membership(group_id='Admins') or \
                          auth.has_permission('update', 'accounting_cashbooks_items')

        header = THEAD(TR(
            TH(T("Date")),
            TH(T("Description")),
            TH(T("Amount")),
            TH(), # Buttons
        ))

        total = 0

        table = TABLE(header, _class="table table-striped table-hover")
        for i, row in enumerate(rows):
            repr_row = list(rows[i:i + 1].render())[0]

            table.append(TR(
                TD(repr_row.BookingDate),
                TD(repr_row.Description),
                TD(self._list_formatted_get_buttons(
                    row,
                    permission_edit,
                ))
            ))

            total += row.Amount

        return dict(
            table=table,
            total=total
        )


    def _list_formatted_get_buttons(self,
                                    row,
                                    permission_edit):
        """
        :param row:
        :param permission_edit:
        :return:
        """
        from os_gui import OsGui

        os_gui = OsGui()
        buttons = DIV(_class='pull-right')

        if permission_edit:
            edit = os_gui.get_button(
                'edit',
                URL('settings', 'financial_costcenter_edit', vars={'acID': row.id})
            )
            buttons.append(edit)
            archive = os_gui.get_button(
                'archive',
                URL('settings', 'financial_costcenter_archive', vars={'acID': row.id})
            )
            buttons.append(archive)

        return buttons

