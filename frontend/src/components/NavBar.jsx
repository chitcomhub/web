import React from 'react';

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
        <a href="/" className="header-menu-item header-menu-item-active">
          Специалисты
        </a>

        <a href="/about" className="header-menu-item ">
          О нас
        </a>
      </div>
      <div className="header-burger" onClick={handleBurgerMenu}>
        <span></span>
      </div>
      <nav className="header-menu">
        <ul className="header-list">
          <li className="header-link">
            <a href="/">Специалисты</a>
          </li>
          <li className="header-link">
            <a href="/about">О нас</a>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default NavBar;
