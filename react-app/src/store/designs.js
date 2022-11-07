import { csrfFetch } from './csrf';
import Cookies from 'js-cookie';

// ACTION TYPES ========================================
const LOAD = 'designs/LOAD';
const LOAD_ONE = 'designs/LOAD_ONE';
const CREATE_DES = 'designs/CREATE_DES';
const UPDATE_DES = 'designs/UPDATE_DES';
const DELETE_DES = 'designs/DELETE_DES';

const CLEAR_DATA = 'designs/CLEAR_DATA';

// ACTIONS =============================================
// get all designs
const load = payload => ({
  type: LOAD,
  payload
});

// get one design
const load_one = designId => ({
  type: LOAD_ONE,
  designId
});

// create design
const create_des = design => ({
  type: CREATE_DES,
  design
});

// update design
const update_des = (designId, design) => ({
  type: UPDATE_DES,
  designId,
  design
});

// delete design
const delete_des = (designId) => ({
  type: DELETE_DES,
  designId
})

// THUNKS ===============================================
// ------------------------ READ ------------------------
// all designs
export const getAllDesigns = () => async dispatch => {
  const response = await fetch('/api/designs/');

  if (response.ok) {
    const designs = await response.json();
    dispatch(load(designs));
  }
};
// user designs
export const getAllUserDesigns = () => async dispatch => {
  const response = await csrfFetch('/api/designs/current');
  // console.log('USER SPOTS RES', response)
  if (response.ok) {
    const userDesigns = await response.json();
    // console.log('USER DES', userDesigns)
    dispatch(load(userDesigns));
  }
};
// single design
export const getADesign = (id) => async dispatch => {
  const response = await fetch(`/api/designs/${id}`);
  // console.log('RESPONSE', response)
  if (response.ok) {
    const des = await response.json();

    dispatch(load_one(des));
    return des;
  }
};

// ------------------------ CREATE ------------------------
export const createDesign = (design) => async dispatch => {
  const response = await fetch('/api/designs/new', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'XSRF-TOKEN': Cookies.get('XSRF-TOKEN')
    },
    body: JSON.stringify(design)
  });

  if (response.ok) {
    const newDesign = await response.json();

    await dispatch(create_des(newDesign));
    return newDesign;
  };
};

// ------------------------ UPDATE ------------------------
export const updateDesign = (designId, design) => async dispatch => {
  const response = await fetch(`/api/designs/${designId}`, {
    method: 'PUT',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(design)
  });
  // console.log('REPONSE for update', response)
  if (response.ok) {
    const updatedDesign = await response.json();
    // console.log('UPDATED DES IN THUNK', updatedDesign)
    dispatch(update_des(designId, updatedDesign));
    // console.log('THIS WAS UPDATED')
    return updatedDesign;
  };
};

// ------------------------ DELETE ------------------------
export const deleteDesign = (designId) => async dispatch => {
  const response = await fetch(`/api/designs/${designId}`, {
    method: 'DELETE'
  });

  if (response.ok) {
    const deleted = await response.json();

    dispatch(delete_des(designId));
    return deleted;
  };
};


// ---- clean up fxn ----
export const clearData = () => ({
  type: CLEAR_DATA
});


// REDUCERS =============================================
const initialState = { allDesigns: {}, singleDesign: {} }


const designReducer = (state = initialState, action) => {
  let newState;
  switch (action.type) {
    case LOAD:
      newState = { ...state, allDesigns: { ...state.allDesigns }, singleDesign: { ...state.singleDesign } };
      const newAllDesigns = {};
      action.payload.Designs.forEach(design => newAllDesigns[design.id] = design);
      newState.allDesigns = newAllDesigns;
      return newState;
    case LOAD_ONE:
      newState = { ...state, allDesigns: { ...state.allDesigns }, singleDesign: { ...state.singleDesign } };
      const newOneDes = action.designId;
      newState.singleDesign = newOneDes;
      return newState;
    case CREATE_DES:
    case UPDATE_DES:
      newState = { ...state, allDesigns: { ...state.allDesigns } };
      const newDesign = action.design;
      newState.singleDesign[action.design.id] = newDesign;
      return newState;
    case DELETE_DES:
      newState = { ...state, allDesigns: { ...state.allDesigns }, singleDesign: { ...state.singleDesign } };
      delete newState.allDesigns[action.designId];
      if (newState.singleDesign.id === action.designId) {
        newState.singleDesign = {}
      }
      // newState = { ...newState };
      return newState;
    default:
      return state;
  }
}

export default designReducer;
