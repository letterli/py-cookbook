#### model 事务


```python
@transation.atomic()
def order_handle(request):
    tran_id = transation.savepoint()
    try:
        transation.savepoint_commit(tran_id)
    except Exception as e:
        transation.savepoint_rollback(tran_id)

```
