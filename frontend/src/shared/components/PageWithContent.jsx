import React, { Fragment } from 'react';
import {Link} from "react-router-dom";

const PageWithContent = ({ title, name, children, breadcrumbPath }) => {
  return (
    <Fragment>
      <div className="row content">
        <div className="col-md-11 section font-white">
          <Link className="font-white" to="/">
            ChitWeb
          </Link>{' '}
          /{' '}
          <Link className="font-white" to={breadcrumbPath}>
            {name}
          </Link>
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
