import { API_BASE_URL } from "../config/index";

const checkStatus = async (response) => {
	if (!response.ok) {
		throw Error(
			response.statusText +
				" | " +
				(await response.text().catch(() => ""))
		);
	}
	return response;
};

export const getAllMembers = async () => {
	return fetch(API_BASE_URL + "/members")
		.then(checkStatus)
		.then((response) => response.json())
		.catch((error) => {
			console.error("Error: " + error);
			return Promise.reject(error);
		});
};
