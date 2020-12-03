% include('header.tpl')

<div class="row">
        <h1 style="text-align: center">Movie Search</h1>
        <div style="width: 25%; margin:25px auto;">

            <form action="/movies" enctype="multipart/form-data">

                <div class="form-group">
                    <label for="film" style="font-size: 18px">Title*</label>
                    <input class="form-control" type="text" name="Title">
                </div>

                <div class="form-group">
                    <label for="length" style="font-size: 18px">ID</label>
                    <input class="form-control" type="number" name="ID">
                </div>

                <div class="form-group">
                    <label for="release_date" style="font-size: 18px"> Released After</label>
                    <input class="form-control" type="date" name="Released After">
                </div>

                <div class="form-group">
                    <label for="release_date" style="font-size: 18px"> Released By</label>
                    <input class="form-control" type="date" name="Released By">
                </div>

                <div class="form-group">
                    <label for="language" style="font-size: 18px">Language</label>
                    <select class="form-control" name="Language">
                        <option></option>
                        % for lan in lans:
                        <option>{{lan[0]}}</option>
                        %end
                    </select>
                </div>

                <hr>
                <div class="form-group">
                    <button class="btn btn-lg btn-primary btn-block">Search</button>
                </div>
            </form>
        </div>
</div>

% include('footer.tpl')


