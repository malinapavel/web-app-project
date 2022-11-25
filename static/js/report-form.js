let link = document.getElementById("reportbtn");
const windowFeatures = "left=600,top=600,width=600,height=600";

link.addEventListener('click', function(event) {
   window.open("{% url 'report_comm' %}", "report_form", windowFeatures);
});