var nj = require('jsnumpy');

var data  = nj.generateRandomNumbers([1000,3,3],0,1000000);

//normalize
for(let i=0;i<data.shape[1];i++){
    console.log('hello')
}