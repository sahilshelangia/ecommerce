  $(document).ready(function(){
  // contact form handler
  var contactForm=$(".contact-form2");
  var contactFormMethod=contactForm.attr("method");
  var contactFormEndPoint=contactForm.attr("action");
  var contactFormSubmitButton=contactForm.find("[type='submit']")
  var contactFormSubmitButtonTxt=contactFormSubmitButton.text();
  function displaySubmitting(doSubmit){
    if(doSubmit){
      contactFormSubmitButton.addClass("disabled");
      contactFormSubmitButton.html("<i class='fa fa-spinner' aria-hidden='true'></i>sending");
    }
    else{           
      contactFormSubmitButton.addClass("disabled");
      contactFormSubmitButton.html(contactFormSubmitButtonTxt);
    }
  }
  contactForm.submit(function(event){
    event.preventDefault();
    var contactFormData=contactForm.serialize();
    var thisForm=$(this)
    displaySubmitting(true);
    $.ajax({
      method:contactFormMethod,
      url:contactFormEndPoint,
      data:contactFormData,

      success:function(data){
        console.log(data);
        alert("Success");
        thisForm[0].reset();
        setTimeout(function(){
          displaySubmitting(false)
        },2000)
      },
      error:function(error){
        console.log(error.responseJSON);
        var jsonData=error.responseJSON;
        var msg="";
        $.each(jsonData,function(key,val){
          msg+=key+":"+val[0].message+"\n";
        })
        alert("Error "+msg);
        setTimeout(function(){
          displaySubmitting(false)
        },2000)
      }
    })
  })




  // Auto search
  var searchForm=$(".search-form");
  var searchInput=searchForm.find("[name='q']");
  var typingTimer;
  var typingInterval=2000;
  var searchBtn=searchForm.find("[type='submit']")

  searchInput.keyup(function(event){
    clearTimeout(typingTimer)
    typingTimer=setTimeout(performSearch,typingInterval);
  })

  searchInput.keydown(function(event){
    clearTimeout(typingTimer)
  })

  function displaySearching(){
    searchBtn.addClass("disabled");
    searchBtn.html("<i class='fa fa-spinner' aria-hidden='true'></i>Searching");
  }
  function performSearch(){
    displaySearching();
    var query=searchInput.val();
    setTimeout(function(){
      window.location.href='/search/?q='+query 
    },3000);
  }

  // cat + add product
  var productForm=$(".form-product-ajax")
  productForm.submit(function(event){
    event.preventDefault()
    console.log("form is not sending")
    var thisForm=$(this)
    var actionEndPoint=thisForm.attr("data-endpoint");
    var httpMethod=thisForm.attr("method");
    var formData=thisForm.serialize();

    $.ajax({
      url: actionEndPoint,
      method: httpMethod,
      data: formData,
      success: function(data){
        var submitSpan=thisForm.find('.submit-span')
        if(data.added){
          submitSpan.html("In Cart <button type='submit' class='btn btn-warning'>Remove</button>");
        }
        else{
          submitSpan.html("<button type='submit' class='btn btn-success'>Add to Cart</button>");
        }
        var navbarCount=$(".navbar-cart-count");
        navbarCount.text(data.cartItemCount);
        var currPath=window.location.href;
        if(currPath.indexOf("cart")!=-1){
          refreshCart();
        }
      },
      error:function(errorData){
        console.log("Error")
        console.log(errorData)
      }
    })         
  })

  function refreshCart(){
    console.log("in curr cart!");
    var cartTable=$('.cart-table');
    var cartBody=cartTable.find('.cart-body');
    var productRows=cartBody.find('.cart-product');
    var currentUrl=window.location.href
    var refreshCartUrl='/api/cart/';
    var refreshCartMethod="GET";
    var data={};
    $.ajax({
      url:refreshCartUrl,
      method:refreshCartMethod,
      data:data,
      success:function(data){
        var hiddenCartItemRemoveForm=$(".cart-item-remove-form")
        if(data.products.length>0){
          productRows.html("");
          i=1;
          $.each(data.products,function(indx,val){
            var newCartItemRemove=hiddenCartItemRemoveForm.clone();
            newCartItemRemove.css("display","block");
            newCartItemRemove.find(".cart-item-product-id").val(val.id);
            cartBody.prepend("<tr><th scope='row'>"+i+"</th><td><a href='"+val.url+"'>"+val.name+"</a>"+newCartItemRemove.html()+"</td><td colspan=3>"+val.price+"</td></tr>")
          })
          cartBody.find('.cart-total').text(data.total);
        }
        else{
          window.location.href=currentUrl;
        }
      },
      error:function(data){
        console.log("Error");
        console.log(data);
      },

    })
  }
})