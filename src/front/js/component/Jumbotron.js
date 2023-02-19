import React from 'react'
import '../../styles/home.css'

export const  Jumbotron= () => {
  return (
    <div className='container-fluid'>
        <div className='row jumbotron'>
          <div className='col-sm-2 col-md-3'></div>
            <div className='col-sm-8 col-md-6  text-center'>
            Conoce la música en vivo de tu localidad y conecta con músicos
            </div>
            <div className='col-sm-2 col-md-3'></div>
        </div>
    </div>
  )
}
