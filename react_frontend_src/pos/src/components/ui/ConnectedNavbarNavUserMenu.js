import { connect } from 'react-redux'
import { injectIntl } from 'react-intl';


import NavbarNavUserMenu from "./NavbarNavUserMenu"

const mapStateToProps = state => 
    ({
        user: state.app.user
    })


const ConnectedNavbarNavUserMenu = injectIntl(connect(
    mapStateToProps
)(NavbarNavUserMenu))

export default ConnectedNavbarNavUserMenu
// TODO: inject intl

// const NavbarUserMenu = ({user, intl}) =>
//     <li className="dropdown user user-menu">
//         <a href="#" className="dropdown-toggle" data-toggle="dropdown">
//             <span>{user.data.first_name}</span>
//         </a>
//         <ul className="dropdown-menu">
//             <li className="user-header">
//                 <img src="/static/images/person.png" className="img-circle" alt="User Image"/>
//                 <p>
//                     {user.data.full_name}
//                     <small></small>
//                 </p>
//             </li>
//             <li className="user-body">
//                 {/* TODO: add change password link */}
//                 <div className="row">
//                     <div className="col-xs-12 text-center">
//                         <a href="/user/change_password?_next=%2Fpos"><i class="fa fa-unlock-alt"></i> {intl.formatMessage({ id: 'app.user.change_password' })}</a>
//                     </div>
//                 </div>
//             </li>
//             <li className="user-footer">
//                 <div className="pull-left">
//                     {/* TODO: add url */}
//                     <a href="/profile" className="btn btn-default btn-flat">{intl.formatMessage({ id: 'app.user.profile' })}</a>
//                 </div>
//                 <div className="pull-right">
//                     {/* TODO: add url */}
//                     <a href="/user/logout" className="btn btn-default btn-flat">{intl.formatMessage({ id: 'app.user.sign_out' })}</a>
//                 </div>
//         </li>
//         </ul>
//     </li>

// export default injectIntl(NavbarUserMenu)