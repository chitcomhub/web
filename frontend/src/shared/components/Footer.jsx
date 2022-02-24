import React from 'react';
import { APP_VERSION } from '../config/index';

const Footer = () => {
  const currentYear = new Date().getFullYear();
  return (
    <div className="row">
      <div className="col-md-12 footer">
        <span>Версия фронтенда {APP_VERSION}</span>
        <br />
        Chechen IT Community &copy; 2019-{currentYear}
      </div>
    </div>
  );
};

export default Footer;
