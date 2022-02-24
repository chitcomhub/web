import PageWithContent from "../shared/components/PageWithContent";

const About = () => {
	return (
		<PageWithContent title="О нас" name="О нас" breadcrumbPath="/about">
			<p className="alert alert-info">
				Информацию о проекте можно получить в группе.
			</p>
		</PageWithContent>
	);
};

export default About;
