import React from 'react'
import logotipo from '../../img/logotipo.png'

export const Footer = () => {
  return (
    <div className='container'>
        <div className='b-example-divider'></div>
        <footer className="row row-cols-1 row-cols-sm-2 row-cols-md-5 py-5 my-5 border-top">
            <div className='col mb-3'>
                <img src={logotipo} href='/' className='d-flex align-items-center mb-3 link-dark text-decoration-none' />
                    
                
                <p className='class="text-muted'>© 2023</p>
            </div>
            <div className='col mb-3'></div>
            <div className='col mb-3'>
                <h5>Secciones</h5>
                <ul className='nav flex-column'>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                </ul>
            </div>
            <div className='col mb-3'>
                <h5>Secciones</h5>
                <ul className='nav flex-column'>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                </ul>
            </div>
            <div className='col mb-3'>
                <h5>Secciones</h5>
                <ul className='nav flex-column'>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                    <li className='nav-item mb-2'>
                        <a href='#' className='nav-link p-0 text-muted'>Home</a>
                    </li>
                </ul>
            </div>

        </footer>
    </div>
  )
}
