import { useEffect } from "react";
import { useHistory } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { getAllBrands, clearData } from "../../store/brands";

import './Brands.css';

import logo from '../../icons/logo.png';

export default function Brands() {
  const brands = useSelector(state => state.brands.allBrands);
  const brandArr = Object.values(brands);

  const dispatch = useDispatch();
  const history = useHistory();

  useEffect(() => {
    dispatch(getAllBrands());

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div className="brand-page">
      <div className='brand-title'>
        <h1>Brand</h1>
        <button onClick={() => history.push('/brand/new')}> + Add new</button>
      </div>
      <div className="brand-container">
        {brandArr.map(brand => (
          <div id='brand-box'>
            <h2
              id='brand-name'
              onClick={()  => history.push(`/brand/${brand.id}`)}
            >{brand.name}</h2>
            <div className="brand-logo-box">
              <h2>Brand logos</h2>
              <div id='logo-pic'>
                <img src={brand.logo} alt='logo' onError={e => e.target.src=logo} />
              </div>
            </div>
            <div className="brand-color-box">
              <h2>Brand colors</h2>
              <div id='indiv-colors'>
                {brand.colors.map(color => (
                  <div id='brand-color-indiv' style={{
                    backgroundColor: `${color.name}`,
                    width: '60px',
                    height: '60px',
                    margin: '5px',
                    border: `1px solid rgb(153,170,179)`,
                    borderRadius: '3px'
                  }}></div>
                ))}
              </div>
            </div>
            <div className="brand-font-box">
              <h2>Brand fonts</h2>
              <div>
                {brand.fonts.map(font => (
                  <>
                  {/* <font face={font.name ?? font.url.normal}
                  >{font.name}</font> */}
                  <div
                  >{font.name}</div>
                  </>
                ))}
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
