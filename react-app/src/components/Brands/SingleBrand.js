import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { getABrand, clearData } from "../../store/brands";
import DeleteBrand from "../DeleteBrandForm/DeleteBrand";

import logo from '../../icons/logo.png';

export default function SingleBrand() {
  const { brandId } = useParams();
  const brand = useSelector(state => state.brands.singleBrand);
  const user = useSelector(state => state.session.user);

  const history = useHistory();
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getABrand(brandId));

    return () => dispatch(clearData())
  }, [dispatch, brandId])

  return (
    <div className="brand-page">
      <div className='brand-title'>
        <h1>Brand</h1>
        {user && user.id === brand.user_id && (
        <div>
        <button onClick={() => history.push(`/brand/${brandId}/edit`)}>Edit brand</button>
        <DeleteBrand />
        </div>
        )}
      </div>
      <div id='brand-box' className="single-brand">
            <h2 id='brand-name'>{brand.name}</h2>
            <div className="brand-logo-box">
              <h2>Brand logos</h2>
              <div id='logo-pic'>
              <img src={brand.logo} alt='logo' onError={e => e.target.src=logo} />

              </div>
            </div>
            <div className="brand-color-box">
              <h2>Brand colors</h2>
              <div id='indiv-colors'>
                {brand.colors && brand.colors.map(color => (
                  <div style={{
                    backgroundColor: `${color.name}`,
                    width: '60px',
                    height: '60px',
                    marginRight: '5px',
                    border: `1px solid rgb(153,170,179)`,
                    borderRadius: '3px'
                  }}></div>
                ))}
              </div>
            </div>
            <div className="brand-font-box">
              <h2>Brand fonts</h2>
              <div>
                {brand.fonts && brand.fonts.map(font => (
                  <div>{font.name}</div>
                ))}
              </div>
            </div>
          </div>
    </div>
  )
}
