 const form = document.getElementById('search-form');

      
 
 form.addEventListener('submit', event => {
   event.preventDefault();

  
   const searchTerm = document.getElementById('team-name').value;


   fetch('/search', {
     method: 'POST',
     body: JSON.stringify({ searchTerm }),
     headers: { 'Content-Type': 'application/json' },
   })
     .then(response => response.json()) 
     .then(data => {
      const pre = document.createElement('result');
      pre.textContent = JSON.stringify(data, null, 2);
    
      document.body.appendChild(pre);
    

      
     });
     
 });
