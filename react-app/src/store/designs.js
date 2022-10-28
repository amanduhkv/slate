import { csrfFetch } from './csrf';
import Cookies from 'js-cookie';

// ACTION TYPES ========================================
const LOAD = 'designs/LOAD';
const CLEAR_DATA = 'designs/CLEAR_DATA';

// ACTIONS
// get all designs
const load = payload => ({
  type: LOAD,
  payload
});


// THUNKS ===============================================
// ---- get all designs ----
export const getAllDesigns = () => async dispatch => {
  const response = await fetch('/api/designs/');

  if (response.ok) {
    const designs = await response.json();
    dispatch(load(designs));
  }
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
    default:
      return state;
  }
}

export default designReducer
