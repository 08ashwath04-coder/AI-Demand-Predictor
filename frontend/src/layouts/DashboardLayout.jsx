import Navbar from '../components/Navbar'; import Sidebar from '../components/Sidebar';
export default function DashboardLayout({role,children}){return <><Navbar/><div className="app-shell"><Sidebar role={role}/><main className="main-content">{children}</main></div></>}
