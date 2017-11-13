
  <script type="text/javascript">
    $(function(){
      
      $('#solve_button').click(function(){
        $.ajax({
                    url: '/post_puzzle',
                    data: $('puzzle_form').serialize(),
                    type: 'POST',
                    success: function(response) {
                        console.log(response);
                      }
                    error: function(error) {
                        console.log(error);
                    }
              )};
      });
    });