import React, { Fragment } from 'react';
import Error from './Error';
import UnitCard from './UnitCard';
import loaderGif from './../assets/images/loader.gif';
import { getAllUnits } from '../util/api';

const UnitFilter = () => {
  const [loading, setLoading] = React.useState(true);
  const [units, setUnits] = React.useState([]);
  const [error, setError] = React.useState('');

  const loadUnits = async () => {
    setLoading(true);
    setError(null);
    try {
      const unitsFromBackend = await getAllUnits();
      setUnits(unitsFromBackend);
    } catch (err) {
      setError('Не удалось связаться с бэкендом (' + err.toString() + ')');
    } finally {
      setLoading(false);
    }
  };

  const handleFilter = (event) => {
    loadUnits();
    event.preventDefault();
  };

  React.useEffect(() => {
    loadUnits();
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
        {!loading && error && <Error text={error}></Error>}
        {!loading && !error && units.map((unit) => <UnitCard key={unit.id} unit={unit} />)}
      </div>

      {/* <div className="row justify-content-center">
        <div className="col-md-3 col-sm-12 col-lg-2 col-12 pagination">
          <span>Показать еще</span>
        </div>
      </div> */}
    </Fragment>
  );
};

export default UnitFilter;
