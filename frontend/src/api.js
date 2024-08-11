/**interceptor */

import axios from "axios"
import { ACCESS_TOKEN  } from "./constants"

const apiUrl = "https://4c3ad919-89f4-4af7-a1c6-64fd100a13d0-dev.e1-us-cdp-2.choreoapis.dev/manga/api/v1"
const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL ? import.meta.env.VITE_API_URL : apiUrl,
})

api.interceptors.request.use(
    (config) => {
        const token = localStorage.getItem(ACCESS_TOKEN);
        if (token) {
            config.headers.Authorization = `Bearer ${token}`
        }
        return config
    },
    (error) => {
        return Promise.reject(error)
    }

)

export default api;