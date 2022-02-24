import React from "react";
import { NavLink } from "react-router-dom";

const LINKS = [
	{ to: "/", title: "Специалисты" },
	{ to: "/about", title: "О нас" },
];

const NavBar = () => {
	const getActiveNavClass = ({ isActive }) => {
		let defaultClass = "header-menu-item";

		if (isActive) {
			defaultClass = `${defaultClass} ${defaultClass}-active`;
		}

		return defaultClass;
	};

	return (
		<header className="row header">
			<div className="col-md-auto col-sm-3 logo-chitweb col-lg-2">
				<a href="/">ChitWeb</a>
			</div>
			<div className="header-splitline align-self-center" />
			<div className="col-md-4 col-6 align-self-center display-switch">
				{LINKS.map(({ to, title }) => (
					<NavLink className={getActiveNavClass} key={to} to={to}>
						{title}
					</NavLink>
				))}
			</div>
		</header>
	);
};

export default NavBar;
