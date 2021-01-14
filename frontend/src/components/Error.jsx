import React from 'react';

const Error = (props) => {
  return (
    <div class="alert alert-danger" role="alert">
        <h4 class="alert-heading">Произошла фатальная ошибка!</h4>
        <p>{props.text}</p>
    </div>
  );
};

export default Error;
