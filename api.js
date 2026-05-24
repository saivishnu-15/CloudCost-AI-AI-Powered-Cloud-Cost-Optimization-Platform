import axios from "axios";

const API = "http://127.0.0.1:8000";

export const getResources = () => axios.get(`${API}/resources`);

export const getWaste = () => axios.get(`${API}/waste`);