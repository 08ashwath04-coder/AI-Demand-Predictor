const API_BASE_URL = import.meta.env.VITE_API_URL ?? 'http://localhost:8000'

async function request(path, options = {}) {
  const headers = { 'Content-Type': 'application/json', ...options.headers }
  const token = localStorage.getItem('token')
  if (token) headers.Authorization = `Bearer ${token}`
  const response = await fetch(`${API_BASE_URL}${path}`, { ...options, headers })
  const body = await response.json().catch(() => ({}))
  if (!response.ok) {
    const error = new Error(body.detail || 'API request failed')
    error.response = { data: body }
    throw error
  }
  return body
}

export const getHealth = () => request('/health')
export const loginUser = (data) => request('/auth/login', { method: 'POST', body: JSON.stringify(data) })
export const registerUser = (data) => request('/auth/register', { method: 'POST', body: JSON.stringify(data) })
export const getFarmerDashboard = () => request('/farmer/dashboard')
export const getFarmerRecommendations = () => request('/farmer/recommendations')
export const getRetailerDashboard = () => request('/retailer/dashboard')
export const getRetailerRecommendations = () => request('/retailer/recommendations')
export const getCalendarByMonth = (month) => request(`/calendar/${month}`)
