$(window).scroll(function() {
    var scroll = $(window).scrollTop(),
      dh = $(document).height(),
      wh = $(window).height();
    scrollPercent = (scroll / (dh - wh)) * 100;
    $('#progressbar').css('height', scrollPercent + '%');
  })
  $(window).scroll(function() {
    var scroll = $(window).scrollTop(),
      dh = $(document).height();
      wh = $(window).height();
      gh = Math.max(dh,wh);
    $('.sidebar').css('height', gh + 'px');
  })
  // $(document).ready(function() {
  //   $('#myTable').dataTable();
  // });
  // $(document).ready(function() {
  //   $('#myTable').dataTable({
  //     'sDom': '"top"i'
  //   });
  // });
  $("#myTable").DataTable({
    "paging": true,
    "ordering": true,
    "searching": true
  });

  function myFunction() {
    // Declare variables
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("myTable");
    tr = table.getElementsByTagName("tr");

    // Loop through all table rows, and hide those who don't match the search query
    for (i = 1; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[0];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
  }
