import { Routes, Route } from "react-router-dom";
import About from "./About";
import Specialists from "./Specialists";

const routes = [
	{
		name: "Home",
		path: "/",
		exact: true,
		component: <Specialists />,
	},
	{
		name: "About us",
		path: "/about",
		component: <About />,
	},
];

export const Router = () => (
	<Routes>
		{routes.map(({ name, path, component }) => (
			<Route key={name} path={path} element={component} />
		))}
	</Routes>
);
