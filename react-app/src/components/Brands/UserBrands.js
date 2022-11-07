import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { getAllUserBrands, clearData } from "../../store/brands";


export default function UserBrands() {
  // const brands = useSelector(state => state.brands.allBrands);


  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(getAllUserBrands());

    return () => dispatch(clearData())
  }, [dispatch])

  return (
    <div>
      <h1>Brand</h1>
      {/* <img
        src={err404}
        alt='err-page'
        style={{
          width: '600px',
          display: 'flex',
          justifyContent: 'center'
        }}
       /> */}
    </div>
  )
}
