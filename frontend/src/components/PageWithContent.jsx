import React, { Fragment } from 'react';

const PageWithContent = (props) => {
  return (
    <Fragment>
      <div className="row content">
        <div className="col-md-11 section" style={{ color: 'white' }}>
          <a style={{ color: 'white' }} href="/">
            ChitWeb
          </a>{' '}
          /{' '}
          <a style={{ color: 'white' }} href="/">
            {props.name}
          </a>
        </div>
      </div>
      <div className="row">
        <div className="col-md-12 aside">{props.title}</div>
      </div>
      {props.children}
    </Fragment>
  );
};

export default PageWithContent;
