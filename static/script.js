$(document).ready(function(){
  readApi();
});
function readApi() {
  // fetch('/memo')
  // .then((res) => console.log(res.json()))
  // .catch(res => alert(res))
  $.ajax({
    type: "GET",
    url: "/memo",
    data: {},
    success: function (response) {
    if (response["result"] == "success") {
      cardMaking(response);
    }}
  })
};
function cardMaking (res){
  responsed_result = res.dbresult
  for (i=0; i < responsed_result.length; i++){
    let htmlCard = `<div class="card" style="width: 18rem; margin: auto;">
      <img src="${responsed_result[i].image}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">${responsed_result[i].title}</h5>
        <p class="card-text">${responsed_result[i].comment}</p>
        <p class="card-text">${responsed_result[i].description}</p>
        <a href="${responsed_result[i].url}" class="btn btn-primary">사이트 바로가기</a>
      </div>
    </div>`
    $("#card").append(htmlCard);
  }
};
function button_control() {
  if ($("#form_control").css("display") == "block") {
    $("#form_control").css({
      'display' : "none",
      'color' : 'red'
    })
    // $("#form_control").hide();
    $("#button_control").text("포스팅 박스 열기");
  }else {
    $("#form_control").show();
    $("#button_control").text("포스팅 박스 닫기");
  }
}
function submit(){
  $.ajax({
    type: "POST",
    url: "/memo",
    data: {
      "url_give" : $("#url_give").val(),
      "comment_give" : $("#comment_give").val()
    },
    success: function(res){
      window.location.reload();
    }
  })
}