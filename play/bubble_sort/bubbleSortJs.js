function bubble_sort(tab){
    
    for(let i=0; i < tab.length; i++){
        for(let j=0; j < tab.length - 1 - i; j++){
            if(tab[j] > tab[j+1]){
                let swap = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = swap
	    }
	}
    }
    return tab
}
 

console.log('Enter list of numbers to test bubble sort')


const readline = require('readline');

// Create an interface to read input and output
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

// Ask the user for input
rl.question('Please enter a list of numbers: ', (input) => {
  
	const tab = input.split(',').map(num => parseInt(num.trim(), 10));
	
	if(tab.some(isNaN)) {
		console.log('one or more are not valid');
	} else {
 		console.log(bubble_sort(tab))
			
	}
	

  // Close the interface
  rl.close();
});


               

