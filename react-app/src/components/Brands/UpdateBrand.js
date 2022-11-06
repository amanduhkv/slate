import { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { updateBrand, getABrand, clearData } from "../../store/brands";

// import './CreateBrand.css';

import { __colors } from "../../assets/colors";
import { __fonts } from "../../assets/fonts";

export default function UpdateBrand() {
  const dispatch = useDispatch();
  const history = useHistory();
  const { brandId } = useParams();
  const user = useSelector(state => state.session.user);
  const brand = useSelector(state => state.brands.singleBrand);

  const [name, setName] = useState(brand.name);
  const [logo, setLogo] = useState(brand.logo);
  const [colors, setColors] = useState(brand.colors);
  const [fonts, setFonts] = useState(brand.fonts);

  const [validationErrs, setValidationErrs] = useState([]);

  if (!user) {
    <h1>Please log in or create an account to update your brand.</h1>
  }

  useEffect(() => {
    dispatch(getABrand(brandId));

    return () => dispatch(clearData())
  }, [dispatch, brandId])

  useEffect(() => {
    const errs = [];

    if (name?.length && name.length < 2) {
      errs.push('Brand names must be at least 2 characters.')
    }
    if (name?.length && name.length > 255) {
      errs.push('This brand name is too long.')
    }
    setValidationErrs(errs);
  }, [name]);

  // inputs original data
  useEffect(() => {
    if(brand) {
      setName(brand.name);
      setLogo(brand.logo);

      const originalColors = [];
      if(brand.colors && brand.colors.length > 0) {
        console.log('brand.colors', brand.colors)
        brand.colors.forEach(color => {
          console.log('COLOR IN CURR BRAND', color)
          originalColors.push(color.name)
          console.log('COLOR ARR', originalColors)
        })
      }
      setColors(originalColors);

      const originalFonts = [];
      if(brand.fonts && brand.fonts.length > 0) {
        brand.fonts.forEach(font => {
          console.log('FONT IN CURR BRAND', font)
          originalFonts.push(font.name)
          console.log('FONT ARR', originalFonts)
        })
      }
      setFonts(originalFonts);
    }
  }, [brand]);

  // inputs checks from original data
  useEffect(() => {
    const currentColors = document.querySelectorAll('#brand-colors');
    // console.log('currentColors', currentColors)
    colors.forEach(color => {
      // console.log('CHECKING COLOR', color)
      currentColors.forEach(checkedColor => {
        // console.log('checkedColor', checkedColor)
        if(checkedColor.value === color.name) checkedColor.checked = true;
      })
    });

    const currFonts = document.querySelectorAll('#brand-fonts');
    fonts.forEach(font => {
      currFonts.forEach(checkedFont => {
        if(checkedFont.value === font.name) checkedFont.checked = true;
      })
    });
  }, [brand, colors, fonts])

  const handleSubmit = async e => {
    e.preventDefault();

    const editBrand = {
      name,
      logo,
      colors,
      fonts
    }
    if (!validationErrs.length) {
      console.log('WORKING')
      console.log('brand', editBrand)
      const updatedBrand = await dispatch(updateBrand(brand.id, editBrand));

      if (updatedBrand) history.push(`/brand/${updatedBrand.id}`);
    };
  }

  return (
    <div>
      <h1 className="title">Update brand</h1>
      <form className="brand-form" onSubmit={handleSubmit}>
        <div id='req'>
          * = required
        </div>

        <label id='brand-tag' for='brand-name-tag'>Brand name *</label>
        <input
          id='brand-name-tag'
          placeholder='Your brand here'
          type='text'
          value={name}
          onChange={e => setName(e.target.value)}
        />

        <label id='brand-tag' for='brand-logo'>Brand logo</label>
        <input
          id='brand-logo'
          type='text'
          value={logo}
          onChange={e => setLogo(e.target.value)}
          placeholder='image.url'
        />

        <label id='brand-tag' for='brand-colors'>Brand colors:</label>
        <div className="color-container">
          {__colors.map((color, idx) => (
            <div key={idx} id={color.alias} className='colors'>
              <input
                type='checkbox'
                id='brand-colors'
                value={color.alias}
                onChange={e => {
                  let colorList = [...colors];
                  console.log('COLORLIST', colorList)
                  if (e.target.checked) {
                    console.log('COLOR TARGET', e.target)
                    colorList = [...colors, e.target.value]
                  }
                  else {
                    colorList.splice(colors.indexOf(e.target.value), 1);
                  }
                  console.log('COLORLIST second', colorList)
                  setColors(colorList)
                }}
              />
              <label
                for={color.alias}
                style={{
                  backgroundColor: `${color.alias}`,
                  color: `white`,
                  padding: '8px',
                  borderRadius: '3px',
                  textShadow: '#000 0 0 10px'
                }}>
                {color.alias}
              </label>
            </div>
          ))}
        </div>


        <label id='brand-tag' for='brand-fonts'>Brand fonts:</label>
        <div className="font-container">
          {__fonts.map(font => (
            <div id={font.family} className='fonts'>
              <input
                type='checkbox'
                id='brand-fonts'
                value={font.family}
                onChange={e => {
                  let fontList = [...fonts];
                  if (e.target.checked) {
                    fontList = [...fonts, e.target.value]
                  }
                  else {
                    const i = fontList.indexOf(e.target.value);
                    fontList.splice(fonts.indexOf(e.target.value), 1);
                  }
                  setFonts(fontList)
                }}
              />
              <label
                for={font.family}
              // style={{
              //   fontFamily: `${font.family}`,
              //   color: `white`,
              //   padding: '8px',
              //   borderRadius: '3px',
              //   textShadow: '#000 0 0 10px'
              // }}
              >
                {font.family}
              </label>
            </div>
          ))}
        </div>

        <button id='brand-submit-button' type='submit'>Update brand</button>
      </form>

    </div>
  )
}
