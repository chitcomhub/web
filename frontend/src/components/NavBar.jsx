import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const LINKS = [
  { to: '/', title: 'Специалисты' },
  { to: '/about', title: 'О нас' },
];

const NavBar = () => {
  const handleBurgerMenu = () => {
    const el = document.querySelector('.header-menu');
    el.classList.toggle('active');
  };

  return (
    <div className="row header">
      <div className="col-md-auto col-sm-3 logo-chitweb col-lg-2">
        <a href="/">ChitWeb</a>
      </div>
      <div className="header-splitline align-self-center"></div>
      <div className="col-md-4 col-6 align-self-center display-switch">
        {LINKS.map(({to, title}) => (
          <NavLink
            exact={true}
            key={to}
            to={to}
            className="header-menu-item"
            activeClassName="header-menu-item-active">
            {title}
          </NavLink>
        ))}
      </div>
      <div className="header-burger" onClick={handleBurgerMenu}>
        <span></span>
      </div>
      <nav className="header-menu">
        <ul className="header-list">
          {LINKS.map(({to, title}) => (
            <li key={to} className="header-link">
              <Link to={to} onClick={handleBurgerMenu}>
                {title}
              </Link>
            </li>
          ))}
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;
