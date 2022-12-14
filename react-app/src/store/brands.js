import { csrfFetch } from './csrf';
import Cookies from 'js-cookie';


// ACTION TYPES ========================================
const LOAD = 'brand/LOAD';
const LOAD_ONE = 'brand/LOAD_ONE';
const CREATE_BRAND = 'brand/CREATE_BRAND';
const UPDATE_BRAND = 'brand/UPDATE_BRAND';
const DELETE_BRAND = 'brand/DELETE_BRAND';

const CLEAR_DATA = 'brand/CLEAR_DATA';

// ACTIONS =============================================
// get all brands
const load = payload => ({
  type: LOAD,
  payload
});

// get one brand
const load_one = brand => ({
  type: LOAD_ONE,
  brand
});

// create brand
const create_brand = brand => ({
  type: CREATE_BRAND,
  brand
});

// update brand
const update_brand = (brandId, brand) => ({
  type: UPDATE_BRAND,
  brandId,
  brand
});

// delete brand
const delete_brand = (brandId) => ({
  type: DELETE_BRAND,
  brandId
})

// THUNKS ===============================================
// ------------------------ READ ------------------------
// all brands
export const getAllBrands = () => async dispatch => {
  const response = await fetch('/api/brand/');

  if (response.ok) {
    const brands = await response.json();
    dispatch(load(brands));
  }
};
// user brands
export const getAllUserBrands = () => async dispatch => {
  const response = await csrfFetch('/api/brand/current');

  if (response.ok) {
    const brands = await response.json();
    dispatch(load(brands));

    return brands;
  }
};
// single brand
export const getABrand = (id) => async dispatch => {
  const response = await fetch(`/api/brand/${id}`);
  // console.log('RESPONSE', response)
  if (response.ok) {
    const brand = await response.json();

    dispatch(load_one(brand));
    return brand;
  }
};

// ------------------------ CREATE ------------------------
export const createBrand = (brand) => async dispatch => {
  const response = await fetch('/api/brand/new', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'XSRF-TOKEN': Cookies.get('XSRF-TOKEN')
    },
    body: JSON.stringify(brand)
  });

  if (response.ok) {
    const newBrand = await response.json();

    await dispatch(create_brand(newBrand));
    return newBrand;
  };
};

// ------------------------ UPDATE ------------------------
export const updateBrand = (brandId, brand) => async dispatch => {
  const response = await fetch(`/api/brand/${brandId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(brand)
  });
  // console.log('REPONSE for update', response)
  if (response.ok) {
    const updatedBrand = await response.json();
    await dispatch(update_brand(brandId, updatedBrand));
    return updatedBrand;
  };
};

// ------------------------ DELETE ------------------------
export const deleteBrand = (brandId) => async dispatch => {
  const response = await fetch(`/api/brand/${brandId}`, {
    method: 'DELETE'
  });

  if (response.ok) {
    const deleted = await response.json();

    dispatch(delete_brand(brandId));
    return deleted;
  };
};


// ---- clean up fxn ----
export const clearData = () => ({
  type: CLEAR_DATA
});



// REDUCERS =============================================
const initialState = { allBrands: {}, singleBrand: {} }


const brandReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case LOAD:
      newState = { ...state, allBrands: { ...state.allBrands }, singleBrand: { ...state.singleBrand } };
      const newAllBrands = {};
      action.payload.Brands.forEach(brand => newAllBrands[brand.id] = brand);
      newState.allBrands = newAllBrands;
      return newState;
    case LOAD_ONE:
      newState = { ...state, allBrands: { ...state.allBrands }, singleBrand: { ...state.singleBrand } };
      const newOneBrand = { ...action.brand };
      newState.singleBrand = newOneBrand;
      return newState;
    case CREATE_BRAND:
    case UPDATE_BRAND:
      newState = { ...state, allBrands: { ...state.allBrands }, singleBrand: { ...state.singleBrand } };
      const newBrand = { ...action.brand };
      newState.singleBrand[action.brand.id] = newBrand;
      return newState;
    case DELETE_BRAND:
      newState = { ...state, allBrands: { ...state.allBrands }, singleBrand: { } };
      delete newState.allBrands[action.brandId];
      newState = { ...newState };
      return newState;
    case CLEAR_DATA:
      return initialState;
    default:
      return state;
  }
}

export default brandReducer;
