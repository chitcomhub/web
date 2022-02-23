import {Switch, Route} from "react-router-dom";
import MemberFilter from "./components/MemberFilter";
import PageWithContent from "./components/PageWithContent";

const routes = [
    {
        name: "Home",
        path: "/",
        exact: true,
        component: () => (
            <PageWithContent
                title="Специалисты"
                name="Специалисты"
                breadcrumbPath="/"
            >
                <MemberFilter />
            </PageWithContent>
        ),
    },
    {
        name: "About us",
        path: "/about",
        component: () => (
            <PageWithContent
                title="О нас"
                name="О нас"
                breadcrumbPath="/about"
            >
                <p className="alert alert-info">Информацию о проекте можно получить в группе.</p>
            </PageWithContent>
        ),
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
