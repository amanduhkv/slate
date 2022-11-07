import err404 from '../icons/err404.svg';

export default function ErrPage() {
  return (
    <>
      <img
        src={err404}
        alt='err-page'
        style={{
          width: '400px',
          display: 'flex',
          justifyContent: 'center',
          margin: '0 auto'
        }}
       />
    </>
  )
}
