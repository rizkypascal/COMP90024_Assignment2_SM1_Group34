/*
  COMP90024 - Group 34 - Semester 1 2022:
  - Juny Kesumadewi (197751); Melbourne, Australia
  - Georgia Lewis (982172); Melbourne, Australia
  - Vilberto Noerjanto (553926); Melbourne, Australia
  - Matilda O’Connell (910394); Melbourne, Australia
  - Rizky Totong (1139981); Melbourne, Australia
*/

const reportWebVitals = onPerfEntry => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS(onPerfEntry);
      getFID(onPerfEntry);
      getFCP(onPerfEntry);
      getLCP(onPerfEntry);
      getTTFB(onPerfEntry);
    });
  }
};

export default reportWebVitals;
