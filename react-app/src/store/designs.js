import { csrfFetch } from './csrf';
import Cookies from 'js-cookie';

// ACTION TYPES
const LOAD = 'designs/LOAD';


// THUNKS
// get all designs
const load = payload => ({
  type: LOAD,
  payload
});



// REDUCERS
const initialState = { allDesigns: {} }
