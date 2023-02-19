import React from 'react'
import '../../styles/home.css'

export const  Jumbotron= () => {
  return (
    <div className='container-fluid'>
        <div className='row jumbotron'>
          <div className='col-sm-1 col-xl-4'></div>
            <div className='col-sm-10 col-xl-4  text-center'>
            Conoce la música en vivo de tu localidad y conecta con músicos
            </div>
            <div className='col-sm-1 col-xl-4'></div>
        </div>
    </div>
  )
}
