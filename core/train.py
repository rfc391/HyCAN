def train_model(model, data_loader, optimizer, scheduler, epochs=10):
    for epoch in range(epochs):
        model.train()
        for batch in data_loader:
            optimizer.zero_grad()
            loss = model(batch['inputs']).mean()
            loss.backward()
            optimizer.step()
        scheduler.step()