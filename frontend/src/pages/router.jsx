import {Switch, Route} from "react-router-dom";
import About from "./About";
import Specialists from "./Specialists";

const routes = [
    {
        name: "Home",
        path: "/",
        exact: true,
        component: Specialists,
    },
    {
        name: "About us",
        path: "/about",
        component: About,
    }
];

export const Router = () => (
    <Switch>
        {routes.map(({ exact = false, component, path, name }) => (
            <Route
                key={name}
                exact={exact}
                path={path}
                component={component}
            />
        ))}
    </Switch>
);
