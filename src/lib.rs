use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use sha_crypt::{sha512_check, sha512_simple, Sha512Params};

#[pyfunction(rounds = "656000")]
fn encrypt(password: &str, rounds: usize) -> PyResult<String> {
    let params =
        Sha512Params::new(rounds).map_err(|err| PyValueError::new_err(format!("{:?}", err)))?;
    let hashed = sha512_simple(password, &params).unwrap();
    Ok(hashed)
}

#[pyfunction]
fn verify(password: &str, hashed_value: &str) -> bool {
    sha512_check(password, hashed_value).is_ok()
}

#[pymodule]
fn sha512_crypt(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(encrypt))?;
    m.add_wrapped(wrap_pyfunction!(verify))?;

    Ok(())
}
