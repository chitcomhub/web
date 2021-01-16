import { API_BASE_URL } from '../config';

const checkStatus = async (response) => {
  if (!response.ok) {
    throw Error(response.statusText + ' | ' + (await response.text().catch(() => '')));
  }
  return response;
};

export const getAllUnits = async () => {
  return fetch(API_BASE_URL + '/units')
    .then(checkStatus)
    .then((response) => response.json())
    .catch((error) => {
      console.error('Error: ' + error);
      return Promise.reject(error);
    });
};
