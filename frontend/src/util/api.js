import { BACKEND_URL } from '../config';

export const getAllUnits = async () => {
  const response = await fetch(BACKEND_URL + '/units');

  const data = await response.json();

  if (data) {
    return data;
  }

  return Promise.reject('Failed to load units from backend');
};
