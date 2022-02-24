import React, { Fragment } from 'react';
import Error from '../../shared/components/Error';
import MemberCard from './MemberCard';
import loaderGif from '../../shared/assets/images/loader.gif';
import { getAllMembers } from '../../shared/util/api';

const MemberFilter = () => {
  const [members, setMembers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState('');

  const loadMembers = async () => {
    setLoading(true);
    setError(null);

    try {
      const membersFromBackend = await getAllMembers();
      setMembers(membersFromBackend);
    } catch (err) {
      setError('Не удалось связаться с бэкендом (' + err.toString() + ')');
    } finally {
      setLoading(false);
    }
  };

  const handleFilter = (event) => {
    loadMembers();
    event.preventDefault();
  };

  React.useEffect(() => {
    loadMembers();
  }, []);

  return (
    <Fragment>
      <div className="block-form">
        <form>
          <div className="row holder">
            <div className="col-md-auto col-lg-auto col-sm-auto col-11 block-form-search">
              <label>Cпециализация</label>
              <select>
                <option>Любая</option>
              </select>
            </div>
            {/* <div className="col-md-auto col-sm-auto col-lg-auto col-11">
              <div className="row">
                <div className="block-form-search">
                  <label>Скилы</label>
                  <input type="text" name="" className="skills search-filter" />
                </div>
              </div>
              <div className="row skill-list">
                <span>java</span>
                <span>android</span>
              </div>
            </div> */}
            <div className="col-md-auto col-sm-auto col-4 align-self-end left-indent col-lg-auto">
              <input
                type="submit"
                value="Отфильтровать"
                className="submit-form"
                onClick={handleFilter}
              />
            </div>
          </div>
        </form>
      </div>

      <div className="row body-chitcom justify-content-around">
        {loading && <img src={loaderGif} alt="Загружаю.." />}
        {!loading && error && <Error text={error} />}
        {!loading && !error && members.map((member) => <MemberCard key={member.id} member={member} />)}
      </div>

      {/* <div className="row justify-content-center">
        <div className="col-md-3 col-sm-12 col-lg-2 col-12 pagination">
          <span>Показать еще</span>
        </div>
      </div> */}
    </Fragment>
  );
};

export default MemberFilter;
