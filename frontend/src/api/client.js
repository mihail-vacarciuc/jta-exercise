import axios from "axios";

export const api = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000',
    timeout: 10000
})

export async function getUsers(params = {}){
    const response = await api.get('/api/users', {params})
    return response.data
}

export async function getUsersAnalytics(params = {}){
    const response = await api.get('/api/users/analytics', {params})
    return response.data
}

export async function getProducts(params = {}){
    const response = await api.get('/api/products', {params})
    return response.data
}

export async function getProductsAnalytics(params = {}){
    const response = await api.get('/api/products/analytics', {params})
    return response.data
}