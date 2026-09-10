import { Navigate, Route, Routes } from 'react-router-dom'
import Home from './pages/Home.jsx'
import Login from './pages/Login.jsx'
import Register from './pages/Register.jsx'
import FarmerDashboard from './pages/FarmerDashboard.jsx'
import RetailerDashboard from './pages/RetailerDashboard.jsx'
import FarmerCalendar from './pages/FarmerCalendar.jsx'
import RetailerCalendar from './pages/RetailerCalendar.jsx'
import Products from './pages/Products/index.jsx'
import Recommendations from './pages/Recommendations/index.jsx'

function App() {
  return <Routes>
    <Route path="/" element={<Home />} />
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
    <Route path="/farmer" element={<FarmerDashboard />} />
    <Route path="/retailer" element={<RetailerDashboard />} />
    <Route path="/farmer/calendar" element={<FarmerCalendar />} />
    <Route path="/retailer/calendar" element={<RetailerCalendar />} />
    <Route path="/products" element={<Products />} />
    <Route path="/recommendations" element={<Recommendations />} />
    <Route path="*" element={<Navigate to="/" replace />} />
  </Routes>
}

export default App
