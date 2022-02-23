import React, { Fragment } from 'react';

const PageWithContent = ({ title, name, children }) => {
  return (
    <Fragment>
      <div className="row content">
        <div className="col-md-11 section" style={{ color: 'white' }}>
          <a style={{ color: 'white' }} href="/">
            ChitWeb
          </a>{' '}
          /{' '}
          <a style={{ color: 'white' }} href="/">
            {name}
          </a>
        </div>
      </div>
      <div className="row">
        <div className="col-md-12 aside">{title}</div>
      </div>
      {children}
    </Fragment>
  );
};

export default PageWithContent;
