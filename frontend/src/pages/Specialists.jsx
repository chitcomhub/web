import PageWithContent from "../shared/components/PageWithContent";
import SpecialistsView from "../modules/specialists-list/SpecialistsView";

const Specialists = () => {
    return (
        <PageWithContent
            title="Специалисты"
            name="Специалисты"
            breadcrumbPath="/"
        >
            <SpecialistsView />
        </PageWithContent>
    );
};

export default Specialists;
