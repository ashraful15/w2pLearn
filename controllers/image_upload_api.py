import os

db.define_table('image_upload',
                Field('image','upload',autodelete=True,uploadfolder=os.path.join(request.folder,'static/images'))                
                )


def image_upload():    
    form = SQLFORM(db.image_upload,
                        fields=['image'],
                        submit_button='Save'
                        )

    # if request.vars.image != None:
    #     form.vars.image_filename = 'fjlksjdflk.jpg' #request.vars.image.filename

    if form.accepts(request.vars):
        response.flash = 'Submitted Successfully '+str(request.vars.image.filename)

    return dict(form=form)


def image_upload_api():
    import time
    import cgi
    import shutil
    upload_file=request.vars.upload_file
    upload_file_name=request.vars.upload_file_name
    
    if upload_file=='':
        return 'Required image'
    else:
        if isinstance(upload_file,cgi.FieldStorage):
            #upload_file_name1 = upload_file.filename               
            upload_file = upload_file.file
            
            if upload_file_name == None:
                #upload_file_name=upload_file_name1
                upload_file_name=str(time.time()).replace('.','')+'.jpg'
            
            shutil.copyfileobj(upload_file, open('E:/web2py/web2py/applications/test/static/images/'+upload_file_name, 'wb'))
            
    return upload_file
    