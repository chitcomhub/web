import React from "react";

const Error = (props) => {
	return (
		<div className="alert alert-danger" role="alert">
			<h4 className="alert-heading">Произошла фатальная ошибка!</h4>
			<p>{props.text}</p>
		</div>
	);
};

export default Error;
