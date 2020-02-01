from CollegeSystem.models import *
from flask import render_template, request


db.create_all()
print("All tables created successfully...!")

#----------------------------------------------------Address------------------------------------------------------------

def dummy_address():
    return Address(id=0, city='', state='', pincode=0)


@app.route('/address/')
def address_welcome_page():
    return render_template('address.html', address=dummy_address(), addresslist=Address.query.all(), college=dummy_college())


@app.route('/address/save/', methods=["POST"])
def save_update_address():
    # msg = ''
    req = request.form
    #  print(req['adrid'])
    #  print(req)
    dbadr = Address.query.filter_by(id=req['adrid']).first()
    #  print(dbadr)
    if dbadr:
        dbadr.city = req['adrcity']
        dbadr.state = req['adrstate']
        dbadr.pincode = req['adrpincode']
        msg = "Address updated successfully...!"
    else:
        adr = Address(id=req['adrid'], city=req['adrcity'], state=req['adrstate'], pincode=req['adrpincode'])
        db.session.add(adr)
        msg="Address added successfully...!"
    db.session.commit()

    return render_template('address.html', address=dummy_address(), addresslist=Address.query.all(), actionmsg=msg, college=dummy_college())


@app.route('/address/edit/<int:adrid>')
def edit_address(adrid):
    return render_template('address.html', address=Address.query.filter_by(id=adrid).first(), addresslist=Address.query.all(), college=dummy_college())


@app.route('/address/delete/<int:adrid>')
def delete_address(adrid):
    dbadr = Address.query.filter_by(id=adrid).first()
    if dbadr:
        db.session.delete(dbadr)
        db.session.commit()
        msg = "Address deleted Successfully...!"
    else:
        msg = "Address not found in database, so cannot delete...!"

    return render_template('address.html', address=dummy_address(), addresslist=Address.query.all(), actionmsg=msg, college=dummy_college())

#----------------------------------------------------College------------------------------------------------------------


def dummy_college():
    return College(id=0, name='', code='', aid=0)


@app.route('/college/')
def college_welcome_page():
    return render_template('address.html', college=dummy_college(), collegelist=College.query.all(), address=dummy_address(), addresslist=Address.query.all())


@app.route('/college/save/', methods=["POST"])
def save_update_college():
    # msg = ''
    req = request.form
    #  print(req['adrid'])
    #  print(req)
    dbclg = College.query.filter_by(id=req['clgid']).first()
    #  print(dbadr)
    if dbclg:
        dbclg.name = req['clgname']
        dbclg.code = req['clgcode']
        dbclg.aid = req['clgadr']
        msg = "College updated successfully...!"
    else:
        clg = College(id=req['clgid'], name=req['clgname'], code=req['clgcode'], aid=req['clgadr'])
        db.session.add(clg)
        msg="College added successfully...!"
    db.session.commit()

    return render_template('address.html', college=dummy_college(), collegelist=College.query.all(), actionmsg=msg, address=dummy_address(), addresslist=Address.query.all())


@app.route('/college/edit/<int:clgid>')
def edit_college(clgid):
    return render_template('address.html', college=College.query.filter_by(id=clgid).first(),
                            collegelist=College.query.all(),
                            address=dummy_address(),
                            addresslist=Address.query.all())


@app.route('/college/delete/<int:clgid>')
def delete_college(clgid):
    dbclg = College.query.filter_by(id=clgid).first()
    if dbclg:
        db.session.delete(dbclg)
        db.session.commit()
        msg = "College deleted Successfully...!"
    else:
        msg = "College not found in database, so cannot delete...!"

    return render_template('address.html', college=dummy_college(), collegelist=College.query.all(), actionmsg=msg, address=dummy_address(), addresslist=Address.query.all())


if __name__ == '__main__':
    app.run(debug=True)